import argparse
import json
import yaml


def get_authors(dbauthjson):
    a = {}
    for record in dbauthjson:
        if record['model'] == 'auth.user':
            a[record['pk']] = {
                'username': record['fields']['username'],
                'first_name': record['fields']['first_name'],
                'last_name': record['fields']['last_name'],
            }
    return a


def fix_categories(f, c):
    new_c = []
    for old_c in f['categories']:
        new_c.append(c[old_c])
    f['categories'] = new_c
    return f


def fix_author(f, a):
    this_author = a[f['created_by']]
    name = "{} {}".format(this_author['first_name'], this_author['last_name'])
    f['created_by'] = name
    return f


def dump_entries(dbjson, authors):
    categories = {}
    for record in dbjson:
        if record['model'] == 'magazine.category':
            categories[record['pk']] = record['fields']['slug']

    for record in dbjson:
        if record['model'] == 'magazine.entry':
            f = fix_categories(record['fields'], categories)
            f = fix_author(record['fields'], authors)
            content = f['content']
            del f['content']
            with open('content/posts/{}.md'.format(f['slug']), 'w') as post:
                post.write('---\n')
                post.write(yaml.dump(f))
                post.write('---\n')
                post.write(content)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='dump gen0 entries')
    parser.add_argument('dbjson', help='The dumped database in json')
    parser.add_argument('dbauthjson', help='The dumped auth database in json')
    args = parser.parse_args()
    with open(args.dbauthjson) as dbauthjson:
        a = get_authors(json.load(dbauthjson))
    with open(args.dbjson) as dbjson:
        dump_entries(json.load(dbjson), a)
