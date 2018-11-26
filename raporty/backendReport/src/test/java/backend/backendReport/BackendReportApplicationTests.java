package backend.backendReport;

import backend.backendReport.model.CompletedOrderReport;
import backend.backendReport.model.Course;
import backend.backendReport.model.DroppedOrderReport;
import backend.backendReport.model.Order;
import backend.backendReport.services.ReportService;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringRunner;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import static org.junit.Assert.assertNotNull;

@RunWith(SpringRunner.class)
@SpringBootTest
public class BackendReportApplicationTests {

	List<Order> orderList = new ArrayList<>();

	@Autowired
	ReportService reportService;
	@Test
	public void contextLoads() {
	}

	@Test
	public void prepareCompletedOrderReportTest(){
		CompletedOrderReport completedOrderReport =reportService.getCompletedOrderReport();
		assertNotNull(completedOrderReport);
	}
	@Test
	public void prepareDropedOrderReportTest(){
		DroppedOrderReport droppedOrderReport =reportService.getDroppedOrderReport();
		assertNotNull(droppedOrderReport);

	}

	public void prepareListCompleted() {
		orderList = Arrays.asList(
				new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Warszawa"),
				new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Gdynia"),
				new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Gdynia"),
				new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Warszawa"),
				new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Warszawa"));
	}
	public void prepareListDropped() {
		orderList = Arrays.asList(new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "anulowane","Gdynia"),
				new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "anulowane","Warszawa"),
				new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "anulowane","Warszawa"),
				new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "anulowane","Warszawa"),
				new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "anulowane","Gdynia"),
				new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "anulowane","Gdynia"));
	}
}
