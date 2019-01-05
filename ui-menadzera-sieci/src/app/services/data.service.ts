import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Employee } from '../models/Employee';
import { Restaurant } from '../models/Restaurant';
import { Recruitment } from '../models/Recruitment';
import { Observable } from 'rxjs/observable';
import 'rxjs/Rx';

@Injectable()
export class DataService {

    private requestOptions = {
        headers: new HttpHeaders({ "Content-Type": "application/json" }),
        withCredentials: true
       };
    constructor(
        public http: HttpClient
    ) { }

    addEmployee(employeeNew: Employee) {
        return this.http.post('http://localhost:9090/dodaj_pracownika', employeeNew);
    }

    dismissEmployee(id:number) {
        return this.http.get(`http://localhost:9090/usun_pracownika?id_pracownika=${id}`); 
    }

    getEmployeesList():Observable<Employee> {
       return this.http.get<Employee>('http://localhost:9090/pobierz_pracownikow', this.requestOptions);
    }

    getRestaurantEmployeesList(id: number):Observable<Employee> {
        return this.http.get<Employee>(`http://localhost:9090/pobierz_pracownikow_restauracji?id_restauracji=${id}`);
    }

    addRecruitment(recruitmentNew: Recruitment) {
        return this.http.post('http://localhost:9090/dodaj_ogloszenie', recruitmentNew);
    }

    getRecruitmentsList():Observable<Recruitment> {
        return this.http.get<Recruitment>(`http://localhost:9090/pobierz_ogloszenia`, this.requestOptions)
    }

    addRestaurant(restaurantNew: Restaurant) {
        return this.http.post('http://localhost:9094/dodaj_restauracje', restaurantNew);
    }

    deleteRestaurant(id) {
        return this.http.post('http://localhost:9094/usun_restauracje', id);
    }

    getRestauranstList():Observable<Restaurant> {
        return this.http.get<Restaurant>('http://localhost:9094/pobierz_restauracje');
    }

    getManagerList():Observable<Employee> {
        return this.http.get<Employee>('http://localhost:9090/pobierz_menadzerow');
    }
/*
    changeManager(newManager: Manager) {
        return this.http.post(`http://localhost:9094/przydziel_menadzera`, newManager);
    }
*/
}
