import { Component, OnInit } from '@angular/core';
import { Restaurant } from '../../models/Restaurant';
import { DataService } from '../../services/data.service';

@Component({
  selector: 'app-manage-restaurant',
  templateUrl: './manage-restaurant.component.html',
  styleUrls: ['./manage-restaurant.component.css']
})
export class ManageRestaurantComponent implements OnInit {

  restaurant: Restaurant = new Restaurant();
  alertString: string = "";

  constructor(public dataService: DataService) {

  }

  ngOnInit() {

  }

  onSubmit() {
    this.dataService.addRestaurant(this.restaurant)
    .subscribe(res => {
      var getValueArray = Object.values(res)
      this.alertString += getValueArray;
      alert(this.alertString.split(',').join(""));
      this.alertString = "";
    });
  }

}
