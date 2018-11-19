package backend.backendReport;

import backend.backendReport.dao.DatabaseAccess;
import backend.backendReport.services.ReportService;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;

@SpringBootApplication
public class BackendReportApplication {

	public static void main(String[] args) {
		SpringApplication.run(BackendReportApplication.class, args);
	}


}
