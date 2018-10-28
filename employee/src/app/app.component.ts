import { Component, OnInit } from '@angular/core';
import { Employee } from './models/employee';
import { DataService } from './services/data.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  title = 'employee';
  employee: Employee = new Employee();

  constructor(
    public dataService:DataService
  ){}

  ngOnInit() {}

  onSubmit({value}:{value:Employee}){
    console.log(value);
    this.dataService.Dodaj_pracownika(this.employee).subscribe(employee => {
      console.log(employee);
    });
  }
}


