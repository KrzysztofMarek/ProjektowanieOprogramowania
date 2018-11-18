import { Injectable } from '@angular/core';
import { RequestOptions, Response } from '@angular/http';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Employee } from '../models/Employee';
import { Recruitment } from '../models/Recruitment';
import { Observable } from 'rxjs';
import 'rxjs/Rx';


@Injectable()
export class DataService {

    private readonly httpOptions = {
            headers: new HttpHeaders({"Content-Type": "application/json"})
    };
    constructor(
        public http: HttpClient
    ) { }

    addEmployee(employee: Employee) {
        return this.http.post('http://localhost:9090/dodajPracownika', employee)
        .subscribe((res:Response) => {
            console.log(res);
            console.log(employee)
          });
    }

    addRecruitment(recruitment: Recruitment) {
        return this.http.post('http://localhost:9090/dodaj_ogloszenie', recruitment)
        .subscribe((res:Response) => {
            console.log(res);
            console.log(recruitment)
          });
    }

    getRecruitmentsList() {
        return this.http.get('http://localhost:9090/pobierz_ogloszenia').
        map(res => res as Recruitment);
    }


}
