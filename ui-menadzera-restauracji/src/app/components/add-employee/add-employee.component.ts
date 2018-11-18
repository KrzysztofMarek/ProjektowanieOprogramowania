import { Component, OnInit } from '@angular/core';
import { Employee } from '../../models/Employee';
import { DataService } from '../../services/data.service';

@Component({
  selector: 'app-add-employee',
  templateUrl: './add-employee.component.html',
  styleUrls: ['./add-employee.component.css']
})
export class AddEmployeeComponent implements OnInit {

  employee: Employee = new Employee();

  constructor(
    public dataService: DataService
  ) { }

  ngOnInit() {

  }

  onSubmit() {
    this.dataService.addEmployee(this.employee);
  }

}
