with open("view.html", "w", encoding="utf-8") as fp:
    for i in range(1, 277):
        fp.write("<img src='" + str(i) + ".webp'><p>P" + str(i) + " translate:</p>\n\n<br><br><br><br><br><br>\n\n")
