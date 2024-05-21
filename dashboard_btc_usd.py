import streamlit as st

def main():
    st.title("Form Registrasi")

    # Membuat input untuk nama
    nama = st.text_input("Nama")

    # Membuat input untuk alamat
    alamat = st.text_area("Alamat")

    # Membuat input untuk nomor telepon
    no_telp = st.text_input("Nomor Telepon")

    # Tombol untuk submit
    if st.button("Submit"):
        if nama and alamat and no_telp:
            st.success("Registrasi berhasil!")
            st.write("Nama:", nama)
            st.write("Alamat:", alamat)
            st.write("Nomor Telepon:", no_telp)
        else:
            st.error("Mohon lengkapi semua informasi.")

    # Tombol untuk memperbarui atau menyegarkan data
    if st.button("Refresh Data"):
        nama = ""
        alamat = ""
        no_telp = ""

if __name__ == "__main__":
    main()
