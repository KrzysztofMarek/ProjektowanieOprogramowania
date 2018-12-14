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
  alertString: string = "";

  constructor(
    public dataService: DataService
  ) { }

  ngOnInit() {
  }

  onSubmit() {
    this.dataService.addEmployee(this.employee)
    .subscribe(res => {
      console.log(res);
      var getValueArray = Object.values(res)
      this.alertString += getValueArray;
      alert(this.alertString.split(',').join(""));
      this.alertString = "";
    });
  }

}
