import { Component, OnInit } from '@angular/core';
import { Employee } from '../../models/Employee';
import { DataService } from '../../services/data.service';

@Component({
  selector: 'app-manage-employee',
  templateUrl: './manage-employee.component.html',
  styleUrls: ['./manage-employee.component.css']
})
export class ManageEmployeeComponent implements OnInit {

  employee: Employee = new Employee();
  employeeNew: Employee = new Employee();
  alertString: string = "";

  constructor(public dataService: DataService) { }

  ngOnInit() {
    this.dataService.getEmployeesList().subscribe(employee => {
      this.employee = JSON.parse(employee['message']);
      console.log(employee);
    });
  }

  onSubmit() {
    console.log(this.employeeNew);
    this.dataService.addEmployee(this.employeeNew)
      .subscribe(res => {
        var getValueArray = Object.values(res)
        this.alertString += getValueArray;
        alert(this.alertString.split(',').join(""));
        this.alertString = "";
        this.dataService.getEmployeesList().subscribe(employee => {
          this.employee = employee;
        });
      });
  }

}
