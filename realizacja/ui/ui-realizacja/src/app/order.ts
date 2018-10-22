import { Course } from './course';

export class Order {

    id: number;
    clientId: number;
    restaurantId: number;
    courseList: Course[];
    price: number;
    orderStatus: string;
    addingDate: Date;
    grade: number;
}
