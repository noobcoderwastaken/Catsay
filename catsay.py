from sys import argv
try:
    text = " ".join(sys.argv[1:])  # Join all command line arguments to form the complete text
    print(f"""\x1b[32;1m
    
                           <| {text.capitalize()} |>
    _._     _,-'""`-._          /
    (,-.`._,'(       |\`-/|   / 
        `-.-' \ )-`( , o o) /
            `-    \`_`"'-

    \x1b[0m""")

except Exception:
    print("Usage: python3 catsay.py <text>")
