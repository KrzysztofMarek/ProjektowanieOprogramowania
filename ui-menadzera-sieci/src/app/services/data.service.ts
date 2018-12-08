import { Injectable } from '@angular/core';
import { RequestOptions, Response } from '@angular/http';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Employee } from '../models/Employee';
import { Restaurant } from '../models/Restaurant';
import { Recruitment } from '../models/Recruitment';
import { Observable } from 'rxjs';
import 'rxjs/Rx';

@Injectable()
export class DataService {

    private readonly httpOptions = {
        headers: new HttpHeaders({ "Content-Type": "application/json" })
    };
    constructor(
        public http: HttpClient
    ) { }

    addEmployee(employee: Employee) {
        return this.http.post('http://localhost:9090/dodaj_pracownika', employee)
    }

    addRecruitment(recruitmentNew: Recruitment) {
        return this.http.post('http://localhost:9090/dodaj_ogloszenie', recruitmentNew);
    }

    getRecruitmentsList() {
        return this.http.get('http://localhost:9090/pobierz_ogloszenia')
            .map(res => res as Recruitment);
    }

    addRestaurant(restaurant: Restaurant) {
        return this.http.post('http://localhost:9094/dodaj_restauracje', restaurant);
    }

}
