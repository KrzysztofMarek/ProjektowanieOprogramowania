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

    addEmployee(employeeNew: Employee) {
        return this.http.post('http://localhost:9090/dodaj_pracownika', employeeNew);
    }

    getEmployeesList():Observable<Employee> {
       let options = new RequestOptions({ withCredentials: true });
       return this.http.get<Employee>('http://localhost:9090/pobierz_pracownikow', options);
    }

    getRestaurantEmployeesList(id: number):Observable<Employee> {
        return this.http.get<Employee>(`http://localhost:9090/pobierz_pracownikow_restauracji?id_restauracji=${id}`);
    }

    addRecruitment(recruitmentNew: Recruitment) {
        return this.http.post('http://localhost:9090/dodaj_ogloszenie', recruitmentNew);
    }

    getRecruitmentsList():Observable<Recruitment> {
        return this.http.get<Recruitment>(`http://localhost:9090/pobierz_ogloszenia`)
    }

    addRestaurant(restaurantNew: Restaurant) {
        return this.http.post('http://localhost:9094/dodaj_restauracje', restaurantNew);
    }

    deleteRestaurant(id:number) {
        return this.http.post('http://localhost:9094/usun_restauracje', id);
    }

    getRestauranstList():Observable<Restaurant> {
        return this.http.get<Restaurant>('http://localhost:9094/pobierz_restauracje');
    }

}
