"""
This script adds a new indicator to this implementation of Open SDG.

Usage example: the following would add 1.1.z, called "My indicator name",
as a new indicator:
    python scripts/batch/add_indicator.py 1.1.z "My indicator name"

What this script actually does:
1. This script creates a file in the _indicators/ folder.
1. This script creates a file each multilingual subfolder of _indicators/.
1. This script creates the global_indicators.yml file in each data/translations
   multilingual subfolder, if it does not already exist.
1. This script adds an entry to each global_indicators.yml file.

What this script does NOT do:
1. This script does not update the data repository. Note that you can use a
   similar script specifically for the data repository.
1. This script does not do any translation.
"""
import sys
import os
import yaml

def get_indicator_content(id, language):
    lines = [
        '---',
        'indicator: ' + id,
        'layout: indicator',
        'permalink: /' + language + '/' + id.replace('.', '-') + '/',
        'language: ' + language,
        '---',
    ]
    return "\n".join(lines)

def get_translation_entry(id, name):
    lines = [
        id + ':',
        '  title: ' + name,
    ]
    return "\n".join(lines)

def add_indicator(id, name):
    # First get all the languages for this site.
    languages = []
    with open('_config.yml', 'r') as stream:
        config = yaml.load(stream)
        languages = config['languages']
    default_language = languages[0]

    # Now write the indicator files.
    for language in languages:
        content = get_indicator_content(id, language)
        filename = id.replace('.', '-') + '.md'
        filepath = os.path.join('_indicators', language, filename)
        # Special case for default language.
        if language == default_language:
            filepath = os.path.join('_indicators', filename)
        f = open(filepath, 'w')
        f.write(content)
        f.close()

    # Now create the translation files if necessary.
    for language in languages:
        filename = 'global_indicators.yml'
        folder = os.path.join('data', 'translations', language)
        os.makedirs(folder, exist_ok=True)
        filepath = os.path.join(folder, filename)
        content = get_translation_entry(id, name)
        f = open(filepath, 'a')
        f.write("\n" + content)
        f.close()

def main():

    # Abort if there is no parameter provided.
    if len(sys.argv) < 3:
        sys.exit('Provide the id number and name of this indicator.')
    id = sys.argv[1]
    name = sys.argv[2]
    add_indicator(id, name)
    print("Remember to update and deploy the data repository first, before deploying this change.")

# Boilerplace syntax for running the main function.
if __name__ == '__main__':
    main()
