@app.route('/przydziel_menadzera', methods=['POST'])
def przydziel_menadzera():
    try:
        rrequest = request.get_json()
        if rrequest['id_pracownika'] is None:
            resp = jsonify(success=False)
            resp.status_code = 404
            return resp
        id_pracownika = rrequest['id_pracownika']

        if rrequest['id_restauracji'] is None:
            resp = jsonify(success=False)
            resp.status_code = 404
            return resp
        id_restauracji = int(rrequest['id_restauracji'])

    except KeyError:
        resp = jsonify(success=False)
        resp.status_code = 404
        return resp

    # odprzydziel starego managera
    for pracownik in lista_pracownikow['lista_pracownikow']:
        if pracownik['stanowisko'] != 'menadzer restauracji':
        	continue
        if pracownik['id_restauracji'] != id_restauracji:
        	continue
        pracownik["id_restauracji"] = 0

    # przydziel nowego managera
    for pracownik in lista_pracownikow['lista_pracownikow']:
        if pracownik["id_pracownika"] != id_pracownika:
            continue

        if pracownik['stanowisko'] != 'menadzer restauracji':
            resp = jsonify('Pracownik o id: ' + str(id_restauracji) + " nie jest menadzerem")
            resp.status_code = 404
            return resp

        pracownik['id_restauracji'] = id_restauracji

        resp = jsonify(success=True)
        resp.status_code = 200
        return resp