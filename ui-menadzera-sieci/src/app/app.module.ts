import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { HttpModule } from '@angular/http';
import { AppComponent } from './app.component';
import { RouterModule, Routes } from '@angular/router';
//Service Imports
import { DataService } from './services/data.service';
import { NavbarComponent } from './components/navbar/navbar.component';
import { HomePageComponent } from './components/home-page/home-page.component';
import { AddRecruitmentComponent } from './components/add-recruitment/add-recruitment.component';
import { ManageEmployeeComponent } from './components/manage-employee/manage-employee.component';
import { ManageRestaurantComponent } from './components/manage-restaurant/manage-restaurant.component';

const appRoutes: Routes = [
  {path:'', component:HomePageComponent},
  {path:'manage_employee', component:ManageEmployeeComponent},
  {path:'manage_restaurant', component:ManageRestaurantComponent},
  {path:'add_recruitment', component:AddRecruitmentComponent}
];

@NgModule({
  declarations: [
    AppComponent,
    NavbarComponent,
    HomePageComponent,
    AddRecruitmentComponent,
    ManageEmployeeComponent,
    ManageRestaurantComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    FormsModule,
    HttpModule,
    RouterModule.forRoot(appRoutes)
  ],
  providers: [DataService],
  bootstrap: [AppComponent]
})
export class AppModule { }
