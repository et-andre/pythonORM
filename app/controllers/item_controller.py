from flask                          import render_template, request, redirect, url_for

from app import app
from app.services.item_service      import ItemService

from app.forms.item.item_new_form   import ItemNewForm

itemService = ItemService()

@app.route('/items')
def getItemList():
    return render_template('items/list.html', items=itemService.find_all())

@app.route('/items/<int:itemid>')
def getItemDetails(itemid):
    return render_template('items/details.html', item=itemService.find_one(itemid))

@app.route('/items/new', methods=["GET", "POST"])
def newItem():
    form = ItemNewForm(request.form)

    if request.method == 'POST':
        if form.validate():
            item = itemService.insert(form)

            return redirect(url_for('getItemDetails', itemid=item.itemid))

    return render_template('items/new.html', form=form)
