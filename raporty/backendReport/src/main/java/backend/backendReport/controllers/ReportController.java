package backend.backendReport.controllers;

import backend.backendReport.interfaces.Report;
import backend.backendReport.model.AverageDeliveryTimeReport;
import backend.backendReport.model.AverageRealisationTimeReport;
import backend.backendReport.model.CompletedOrderReport;
import backend.backendReport.model.DroppedOrderReport;
import backend.backendReport.services.ReportService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

/**
 * Created by Piotr on 2018-11-19.
 */

@RestController
public class ReportController implements Report {

    ReportService reportService;

    @Autowired
    public ReportController(ReportService reportService) {
        this.reportService = reportService;
    }

    @RequestMapping(value = "/fetch-completed-order-report", method = RequestMethod.GET, produces = "application/json")
    public CompletedOrderReport getCompletedOrderReport() {
        return reportService.getCompletedOrderReport();
    }

    @RequestMapping(value = "/fetch-dropped-order-report", method = RequestMethod.GET, produces = "application/json")
    public DroppedOrderReport getDroppedOrderReport() {
        return reportService.getDroppedOrderReport();
    }

    @RequestMapping(value = "/fetch-average-realisation-time", method = RequestMethod.GET, produces = "application/json")
    public AverageRealisationTimeReport getAverageRealisationTime() {
        return reportService.getAverageRealisationTimeReport();
    }

    @RequestMapping(value = "/fetch-average-delivery-time", method = RequestMethod.GET, produces = "application/json")
    public AverageDeliveryTimeReport getAverageDeliveryTime() {
        return reportService.getAverageDeliveryTimeReport();
    }

    @RequestMapping(value = "/create-completed-order-report-pdf", method = RequestMethod.GET, produces = "application/json")
    public ResponseEntity<byte[]> createCompletedOrderPdf() {
        HttpHeaders headers = new HttpHeaders();
        headers.add("Content-Type", "application/pdf");
        headers.add("Content-Disposition", "attachment; filename=report.pdf");
        headers.add("Access-Control-Allow-Headers", "Content-Disposition, Content-Type");
        return new ResponseEntity<>(reportService.createCompletedOrderPdf(), headers, HttpStatus.CREATED);

    }
    @RequestMapping(value = "/create-dropped-order-report-pdf", method = RequestMethod.GET, produces = "application/json")
    public ResponseEntity<byte[]> createDroppedOrderPdf() {
        HttpHeaders headers = new HttpHeaders();
        headers.add("Content-Type", "application/pdf");
        headers.add("Content-Disposition", "attachment; filename=report.pdf");
        headers.add("Access-Control-Allow-Headers", "Content-Disposition, Content-Type");
        return new ResponseEntity<>(reportService.createDroppedOrderPdf(), headers, HttpStatus.CREATED);
    }
    @RequestMapping(value = "/create-average-realisation-time-pdf", method = RequestMethod.GET, produces = "application/json")
    public ResponseEntity<byte[]> createAverageRealisationOrderPdf() {
        HttpHeaders headers = new HttpHeaders();
        headers.add("Content-Type", "application/pdf");
        headers.add("Content-Disposition", "attachment; filename=report.pdf");
        headers.add("Access-Control-Allow-Headers", "Content-Disposition, Content-Type");
        return new ResponseEntity<>(reportService.createAverageRealisationTimePdf(), headers, HttpStatus.CREATED);
    }
    @RequestMapping(value = "/create-average-delivery-time-pdf", method = RequestMethod.GET, produces = "application/json")
    public ResponseEntity<byte[]> createAverageDeliveryOrderPdf() {
        HttpHeaders headers = new HttpHeaders();
        headers.add("Content-Type", "application/pdf");
        headers.add("Content-Disposition", "attachment; filename=report.pdf");
        headers.add("Access-Control-Allow-Headers", "Content-Disposition, Content-Type");
        return new ResponseEntity<>(reportService.createAverageDeliveryTimePdf(), headers, HttpStatus.CREATED);
    }
}
