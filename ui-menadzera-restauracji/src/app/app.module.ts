import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { HttpModule } from '@angular/http';
import { AppComponent } from './app.component';
import { RouterModule, Routes } from '@angular/router';
//Service Imports
import { DataService } from './services/data.service';
import { AddEmployeeComponent } from './components/add-employee/add-employee.component';
import { NavbarComponent } from './components/navbar/navbar.component';
import { AddRecruitmentComponent } from './components/add-recruitment/add-recruitment.component';
import { HomepageComponent } from './components/homepage/homepage.component';
import { ManageEmployeeComponent } from './components/manage-employee/manage-employee.component';

const appRoutes: Routes = [
  {path:'', component:HomepageComponent},
  {path:'manage_employee', component:ManageEmployeeComponent},
  {path:'add_recruitment', component:AddRecruitmentComponent}
];

@NgModule({
  declarations: [
    AppComponent,
    AddEmployeeComponent,
    NavbarComponent,
    AddRecruitmentComponent,
    HomepageComponent,
    ManageEmployeeComponent
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
