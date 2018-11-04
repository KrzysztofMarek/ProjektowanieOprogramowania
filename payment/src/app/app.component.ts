import { Component } from '@angular/core';
import { Payment } from './models/payment';
import { DataService } from './services/data.service';
import { Observable } from 'rxjs';
import { interval } from 'rxjs';
import {  } from 'rxjs';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'payment';
  payment: Payment = new Payment();
  paymentOptions: any = [
    'Karta',
    'Blik',
    'Przelew24'
  ];
  status: string;

  constructor(public dataService: DataService) { }

  ngOnInit() { 
    interval(1000)
    .subscribe(res => {
    this.dataService.getStatus();
    });
  }

  onSubmit() {
    this.onNavigate();
    console.log(this.payment);
    this.dataService.pay(this.payment);
  }

  onNavigate() {
    window.open("http://localhost:4202/", "_blank");
  }
  radioChangeHandler(event: any) {
    this.payment.sposob_zaplaty = event.target.value;
  }
}
