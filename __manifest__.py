{
    'name': 'MC Tiers Dashboard',
    'version': '1.0',
    'depends': ['base', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'views/menus.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'mc_tiers/static/src/scss/style.scss',
            'mc_tiers/static/src/js/ranking_board.js',
            'mc_tiers/static/src/xml/ranking_board.xml',
        ],
    },
    'installable': True,
    'application': True,
}