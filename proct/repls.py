[
    (
        # Números de telefone
        r'((?:\+55 )?\(?(\d\d)\)?[\. -](\d)[\. -]?(\d{4})[\. -]?(\d{4}))',
        r'<a href="tel:+55\2\3\4\5">\1</a>'
    ),
    (
        # E-mails
        r'([\w\.+-]+@([\w-]+\.)+[a-z]{2,})',
        r'<a href="mailto:\1">\1</a>'
    ),
    (
        # Datas
        r'(([012]?\d|3[012])/(0?\d|1[012])/\d{4})',
        r'<span class="date">\1</span>'
    ),
    (
        # Embed YouTube step 1
        r'https?://www\.youtube\.com/watch\?v=(\w+)',
        r'[YOUTUBE:\1]',
    ),
    (
        # Links
        r'(https?://\S*[^\s\.,\)])',
        r'<a href="\1">\1</a>',
    ),
    (
        # Imagem
        r'>(https?://[^<]*\.(png|jpg|jpeg|gif|svg|svgz))<',
        r'><img src="\1" style="max-width:300px;max-height:200px" /><',
    ),
    (
        # Embed do YouTube step 2
        r'\[YOUTUBE:(\w+)\]',
        r'<iframe width="560" height="315" src="https://www.youtube.com/embed/\1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'
    ),
    (
        # Parágrafos
        r'(\n\n|^)',
        r'\1<p>',
    ),
    (
        # Parágrafos
        r'(<p>.*)',
        r'\1</p>',
    ),
    (
        # Linhas horizontais
        r'<p>-{5,}</p>',
        r'<hr />',
    ),
    (
        # Cidades
        r"([A-Z]\w+ ((d'|d[eao]s? )?[A-Z]\w+ )*- "
        "(AC|AL|AP|AM|BA|CE|DF|ES|GO|MA|MT|MS|MG|PA|PB|PR|"
        "PE|PI|RJ|RN|RS|RO|RR|SC|SP|SE|TO))",
        r'<a href="https://www.google.com.br/maps/place/\1">\1</a>'
    ),
]
