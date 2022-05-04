from flask import Blueprint, render_template
from flask_login import current_user, login_required
from app.database.queries import loans_with_overdo
from app import Library as DB

admin = Blueprint('admin', __name__)


@admin.route('/Librarian')
@login_required
def main():
    loans = loans_with_overdo(DB)
    return render_template('Librarian.html', name = current_user.name, loans = loans)