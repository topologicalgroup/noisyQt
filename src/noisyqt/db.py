import sqlite3
import datetime
import io
from PIL import Image

DB_SCHEMA = """
CREATE TABLE IF NOT EXISTS images (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    filename TEXT NOT NULL,
    original BLOB NOT NULL,
    denoised BLOB NOT NULL,
    created_at TEXT NOT NULL
);
"""

def image_to_byte_array(image: Image.Image) -> bytes:
    img_byte_array = io.BytesIO()
    # TODO: fix image.format
    # Assume it'll be in png for now
    image.save(img_byte_array, format="PNG")
    img_byte_array = img_byte_array.getvalue()
    return img_byte_array

def byte_array_to_image(byte_array: bytes) -> Image.Image: 
    image = Image.open(io.BytesIO(byte_array))
    return image

class Database:
    """ Database 
        An SQLite implementation for file handling. Input should be in Image (PIL). This class
        will handle converting it into byte arrays to and from.

    Args:
        db_file_path(str): path to where the .db file will be made

    Methods:
        insert(filename, original, denoised)
        read(id) -> Image
    """

    def __init__(self, db_file_path) -> None:
        self.conn = sqlite3.connect(db_file_path)
        cursor = self.conn.cursor()
        cursor.execute(DB_SCHEMA)
        self.conn.commit()

    def insert(self, filename: str, original: Image.Image, denoised: Image.Image):
        original_bytes = image_to_byte_array(original)
        denoised_bytes = image_to_byte_array(denoised)
        date_now = datetime.datetime.now().isoformat()
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO images (filename, original, denoised, created_at) " +
                       "VALUES (?, ?, ?, ?)",(filename, original_bytes, denoised_bytes, date_now))
        self.conn.commit()

    def read(self, id: int):
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, filename, original, denoised, created_at FROM images WHERE id = ?", (id,))
        row = cursor.fetchone()

        if not row:
            print(f"Could not fetch data for id '{id}'")
            return None

        res = {"id": row[0],
               "filename": row[1],
               "original": row[2],
               "denoised": row[3],
               "created_at": row[4]}
        return res

    def read_all(self):
        pass

    def delete(self, id: int):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM images WHERE id = ?", (id,))
        if cursor.rowcount != 1:
            print(f"Failed to delete row with id: '{id}")
        else:
            print(f"Successfully deleted row id: '{id}")

    def close(self):
        self.conn.close()
