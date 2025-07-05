# scripts/import_demo.py

import json
from app import create_app, db
from app.models import Landing

app = create_app()

def import_landing():
    with app.app_context():
        with open('demo/landing.json', 'r', encoding='utf-8') as f:
            data = json.load(f)

        existing = Landing.query.filter_by(slug=data['slug']).first()
        if existing:
            print(f"La landing '{data['slug']}' ya existe.")
            return

        landing = Landing(
            slug=data['slug'],
            theme=data['theme'],
            fields=data['fields']
        )
        db.session.add(landing)
        db.session.commit()
        print(f"Landing '{landing.slug}' importada correctamente.")

if __name__ == '__main__':
    import_landing()

