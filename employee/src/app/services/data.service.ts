import { Injectable } from '@angular/core';
import { Headers, RequestOptions, Response, Http } from '@angular/http';
import { HttpClient } from '@angular/common/http';
import { Employee } from '../models/Employee';

@Injectable()
export class DataService {

    constructor(
        public http: Http
    ) { }

    Dodaj_pracownika(employee: Employee) {


        let headers = new Headers();
        headers.append('Accept', 'application/json')
        headers.append("Access-Control-Allow-Origin", "*");
    
        let options = new RequestOptions();
        options.headers = headers;

        return this.http.post('http://localhost:9090/dodajPracownika', employee, options)
    }
}
