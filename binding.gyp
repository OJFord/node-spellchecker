{
  'variables': {
    'spellchecker_use_hunspell': 'true',
    'conditions': [
      ['OS=="mac"', {
        'spellchecker_use_hunspell': 'false',
      }],
    ],
  },
  'targets': [
    {
      'target_name': 'spellchecker',
      'sources': [
        'src/main.cc',
      ],
      'conditions': [
        ['spellchecker_use_hunspell=="true"', {
          'dependencies': [
            'hunspell',
          ],
          'sources': [
            'src/spellchecker_hunspell.cc',
          ],
        }],
        ['OS=="mac" and spellchecker_use_hunspell=="false"', {
          'sources': [
            'src/spellchecker_mac.mm',
          ],
          'link_settings': {
            'libraries': [
              '$(SDKROOT)/System/Library/Frameworks/AppKit.framework',
            ],
          },
        }],
      ],
    },
  ],
  'conditions': [
    ['spellchecker_use_hunspell=="true"', {
      'targets': [
        {
          'target_name': 'hunspell',
          'type': 'static_library',
          'msvs_guid': 'D5E8DCB2-9C61-446F-8BEE-B18CA0E0936E',
          'defines': [
            'HUNSPELL_STATIC',
          ],
          'sources': [
            'vendor/hunspell/src/hunspell/affentry.cxx',
            'vendor/hunspell/src/hunspell/affentry.hxx',
            'vendor/hunspell/src/hunspell/affixmgr.cxx',
            'vendor/hunspell/src/hunspell/affixmgr.hxx',
            'vendor/hunspell/src/hunspell/atypes.hxx',
            'vendor/hunspell/src/hunspell/baseaffix.hxx',
            'vendor/hunspell/src/hunspell/csutil.cxx',
            'vendor/hunspell/src/hunspell/csutil.hxx',
            'vendor/hunspell/src/hunspell/dictmgr.cxx',
            'vendor/hunspell/src/hunspell/dictmgr.hxx',
            'vendor/hunspell/src/hunspell/filemgr.cxx',
            'vendor/hunspell/src/hunspell/filemgr.hxx',
            'vendor/hunspell/src/hunspell/hashmgr.cxx',
            'vendor/hunspell/src/hunspell/hashmgr.hxx',
            'vendor/hunspell/src/hunspell/htypes.hxx',
            'vendor/hunspell/src/hunspell/hunspell.cxx',
            'vendor/hunspell/src/hunspell/hunspell.h',
            'vendor/hunspell/src/hunspell/hunspell.hxx',
            'vendor/hunspell/src/hunspell/hunzip.cxx',
            'vendor/hunspell/src/hunspell/hunzip.hxx',
            'vendor/hunspell/src/hunspell/langnum.hxx',
            'vendor/hunspell/src/hunspell/phonet.cxx',
            'vendor/hunspell/src/hunspell/phonet.hxx',
            'vendor/hunspell/src/hunspell/replist.cxx',
            'vendor/hunspell/src/hunspell/replist.hxx',
            'vendor/hunspell/src/hunspell/suggestmgr.cxx',
            'vendor/hunspell/src/hunspell/suggestmgr.hxx',
            'vendor/hunspell/src/hunspell/utf_info.hxx',
            'vendor/hunspell/src/hunspell/w_char.hxx',
            'vendor/hunspell/src/parsers/textparser.cxx',
            'vendor/hunspell/src/parsers/textparser.hxx',
          ],
          'direct_dependent_settings': {
            'defines': [
              'HUNSPELL_STATIC',
              'USE_HUNSPELL',
            ],
          },
        }
      ],
    }],
  ],
}
