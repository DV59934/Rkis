text = "asddfnka"
if text[:3] == "abc":
    text = text.replace("abc", "www")
else:
    text += "www"
print(text)