import { Component, OnInit  } from '@angular/core';
import { Payment } from './models/payment';
import { DataService } from './services/data.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  title = 'payment';
  payment: Payment = new Payment();

  constructor(
    public dataService:DataService
  ){}

  ngOnInit() {}

  onSubmit(){
    this.dataService.pay();
  }
}
