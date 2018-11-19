import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { AppComponent } from './app.component';
import { HttpServiceImpl } from './services/http.service.impl';
import { CommonModule } from '@angular/common';
import { ChartModule } from 'primeng/chart';

@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    CommonModule,
    ChartModule
  ],
  providers: [HttpServiceImpl],
  bootstrap: [AppComponent]
})
export class AppModule { }
