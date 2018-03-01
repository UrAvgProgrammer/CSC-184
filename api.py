from bottle import run, get, post, request, delete, put

guns = [{'Name': 'AR15', 'Type': 'Rifle'},
        {'Name': 'M4A1', 'Type': 'Rifle'},
        {'Name': 'M14EBR', 'Type': 'Rifle'},
        {'Name': 'AKM', 'Type': 'Rifle'},
        {'Name': 'Thompson', 'Type': 'SMG'},
        {'Name': 'MP7', 'Type': 'SMG'},
        {'Name': 'PP19', 'Type': 'SMG'},
        {'Name': 'P90', 'Type': 'SMG'},
        {'Name': 'SAIGA-12', 'Type': 'Shotgun'},
        {'Name': 'M870', 'Type': 'Shotgun'},
        {'Name': 'M1887', 'Type': 'Shotgun'},
        ]


@get('/')
def show_all():
    return {'Guns': guns}


@get('/guns/<name>')
def one_gun(name):
    the_gun = [gun for gun in guns if gun['Name'] == name]
    return {'Guns': the_gun[0]}


@post('/')
def add_gun():
    new_gun = {'Name': request.json.get('Name'), 'Type': request.json.get('Type')}
    guns.append(new_gun)
    return {'Guns': guns}


@put('/guns/<name>')
def edit_one(name):
    the_gun = [gun for gun in guns if gun['Name'] == name]
    the_gun[0]['Name'] = request.json.get('Name')
    the_gun[0]['Type'] = request.json.get('Type')
    return {'Guns': the_gun[0]}


@delete('/guns/<name>')
def delete_one(name):
    the_gun = [gun for gun in guns if gun['Name'] == name]
    guns.remove(the_gun[0])
    return {'Guns': guns}


run(reloader=True, debug=True, port=5000)
