def generateHTML(mapping_dict):
    print('\n')
    print("Generating HTML.....")
    print('\n')
    htmlFile = open('diagram.html', 'w')
    htmlFile.write(''' <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="utf-8">
    <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
    <script>mermaid.initialize({ startOnLoad: true });</script>
    <style>svg{max-width: inherit !important; min-width: 10000px;}</style>
    </head>
    <body>
    <div class="mermaid">\nerDiagram\n    ''')
    for table in mapping_dict:
        for dependency in mapping_dict[table]:
            htmlFile.write(table+" }|..|{ "+dependency['table']+" : "+ dependency['column'] + " \n")
        
        # If no foreign keys were present
        if len(mapping_dict[table]) == 0:
            htmlFile.write(table + " \n")
    htmlFile.write('''</div>    
    </body>
    </html>''')
    htmlFile.close()
    print("HTML Generated successfully.\n")
