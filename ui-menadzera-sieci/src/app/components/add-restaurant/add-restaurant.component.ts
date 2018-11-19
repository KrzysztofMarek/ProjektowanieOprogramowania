import { Component, OnInit } from '@angular/core';
import { Restaurant } from '../../models/Restaurant';
import { DataService } from '../../services/data.service';

@Component({
  selector: 'app-add-restaurant',
  templateUrl: './add-restaurant.component.html',
  styleUrls: ['./add-restaurant.component.css']
})
export class AddRestaurantComponent implements OnInit {

  restaurant: Restaurant = new Restaurant();

  constructor(public dataService: DataService) {

  }

  ngOnInit() {

  }

  onSubmit() {
    this.dataService.addRestaurant(this.restaurant);
  }
  
  onCancel() {
    
  }

}
