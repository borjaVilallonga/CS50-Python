# input
fr = input("File name: ")

# limpiar input
fr = fr.strip().lower()

# hacer condicion
if fr.endswith(".gif"):
    print("image/gif")
elif fr.endswith(".jpg") or fr.endswith(".jpeg"):
    print("image/jpeg")
elif fr.endswith(".png"):
    print("image/png")
elif fr.endswith(".pdf"):
    print("application/pdf")
elif fr.endswith(".txt"):
    print("text/plain")
elif fr.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")
