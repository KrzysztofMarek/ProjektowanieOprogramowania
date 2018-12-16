import { Component, OnInit } from '@angular/core';
import { Restaurant } from '../../models/Restaurant';
import { Employee } from '../../models/Employee';
import { DataService } from '../../services/data.service';

@Component({
  selector: 'app-manage-restaurant',
  templateUrl: './manage-restaurant.component.html',
  styleUrls: ['./manage-restaurant.component.css']
})
export class ManageRestaurantComponent implements OnInit {

  employee: Employee = new Employee();
  restaurant: Restaurant = new Restaurant();
  restaurantNew: Restaurant = new Restaurant();
  alertString: string = "";

  constructor(public dataService: DataService) {

  }

  ngOnInit() {
    this.dataService.getRestauranstList().subscribe(restaurant => {
      this.restaurant = JSON.parse(restaurant['message']);
      console.log(this.restaurant)
    });
  }

  onSubmit() {
    this.dataService.addRestaurant(this.restaurantNew)
      .subscribe(res => {
        var getValueArray = Object.values(res)
        this.alertString += getValueArray;
        alert(this.alertString.split(',').join(""));
        this.alertString = "";
        this.dataService.getRestauranstList().subscribe(restaurant => {
          this.restaurant = restaurant;
        });
      });
  }

  onClick(rest) {
    console.log(rest.id_restauracji);
    this.dataService.getRestaurantEmployeesList(rest.id_restauracji).subscribe(employees => {
      this.employee = JSON.parse(employees['message']);
      console.log(this.employee);
    });
  }

  onDelete(rest) {
    console.log(rest.id_restauracji);
    if (confirm("Czy napewno chcesz usunąć restaurację?")) {
      this.dataService.deleteRestaurant(rest.id_restauracji);
      this.dataService.getRestauranstList().subscribe(restaurant => {
        this.restaurant = JSON.parse(restaurant['message']);
        console.log(this.restaurant)
      });
    }
  }

}
