import streamlit as st
from PIL import Image
import io
import os
import math
import tempfile
import zipfile

def equirectangular_to_cubemap(source_image, cube_size):
    width = source_image.width
    height = source_image.height
    faces = [Image.new('RGB', (cube_size, cube_size)) for _ in range(6)]

    rotations = [-90, 90, 0, 180, 90, -90]
    new_order = [5, 4, 0, 1, 2, 3]

    for y in range(cube_size):
        for x in range(cube_size):
            nx = (x + 0.5) / cube_size * 2 - 1
            ny = (y + 0.5) / cube_size * 2 - 1

            vectors = [
                [1.0, ny, -nx],
                [-1.0, ny, nx],
                [-ny, 1.0, -nx],
                [-ny, -1.0, nx],
                [-ny, nx, 1.0],
                [-ny, -nx, -1.0]
            ]

            for original_idx, new_idx in enumerate(new_order):
                vec = vectors[original_idx]
                face = faces[new_idx]
                pixels = face.load()

                r = math.sqrt(sum(c**2 for c in vec))
                theta = math.acos(vec[2] / r)
                phi = math.atan2(vec[1], vec[0])

                u = ((phi + math.pi) / (2 * math.pi)) * width
                v = (theta / math.pi) * height

                u1 = int(u) % width
                v1 = int(v) % height
                pixels[x, y] = source_image.getpixel((u1, v1))

    rotated_faces = [face.rotate(rot) for face, rot in zip(faces, rotations)]
    return rotated_faces

def stitch_faces(faces, cube_size):
    result = Image.new('RGB', (cube_size * 6, cube_size))
    for i, face in enumerate(faces):
        result.paste(face, (i * cube_size, 0))
    return result

st.title("360° Panorama to Cubemap Converter")

uploaded = st.file_uploader("Upload a 360° equirectangular image", type=["jpg", "jpeg", "png"])
cube_size = st.slider("Cubemap Face Size (px)", 256, 2048, 512, step=256)

if uploaded:
    image = Image.open(uploaded).convert('RGB')
    st.image(image, caption="Input 360° Image", use_column_width=True)

    with st.spinner("Converting to cubemap..."):
        faces = equirectangular_to_cubemap(image, cube_size)
        stitched = stitch_faces(faces, cube_size)

    st.image(stitched, caption="Stitched Cubemap", use_column_width=True)

    # Prepare download
    with tempfile.TemporaryDirectory() as tmpdir:
        zip_path = os.path.join(tmpdir, "cubemap_faces.zip")
        with zipfile.ZipFile(zip_path, 'w') as zipf:
            for idx, face in enumerate(faces):
                fname = f"face_{idx + 1}.jpg"
                fpath = os.path.join(tmpdir, fname)
                face.save(fpath)
                zipf.write(fpath, fname)
        with open(zip_path, "rb") as f:
            st.download_button("Download Faces as ZIP", f, file_name="cubemap_faces.zip")

