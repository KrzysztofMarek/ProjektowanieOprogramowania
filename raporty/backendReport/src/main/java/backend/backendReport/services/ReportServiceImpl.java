package backend.backendReport.services;

import backend.backendReport.dao.DatabaseAccess;
import backend.backendReport.model.*;
import com.itextpdf.text.Document;
import com.itextpdf.text.pdf.DefaultFontMapper;
import com.itextpdf.text.pdf.PdfContentByte;
import com.itextpdf.text.pdf.PdfTemplate;
import com.itextpdf.text.pdf.PdfWriter;
import org.jfree.chart.ChartFactory;
import org.jfree.chart.JFreeChart;
import org.jfree.chart.plot.PlotOrientation;
import org.jfree.data.category.DefaultCategoryDataset;
import org.jfree.data.general.DefaultPieDataset;
import org.springframework.stereotype.Service;

import java.awt.*;
import java.awt.geom.Rectangle2D;
import java.io.ByteArrayOutputStream;
import java.io.FileOutputStream;
import java.util.LinkedList;
import java.util.List;

/**
 * Created by Piotr on 2018-11-19.
 */

@Service
public class ReportServiceImpl implements ReportService {

    DatabaseAccess databaseAccess;


    public ReportServiceImpl(DatabaseAccess databaseAccess) {
        this.databaseAccess = databaseAccess;
    }

    @Override
    public CompletedOrderReport getCompletedOrderReport() {
        return prepareCompletedOrderReport();
    }

    @Override
    public DroppedOrderReport getDroppedOrderReport() {
        return prepareDroppedOrderReport();
    }

    @Override
    public AverageRealisationTimeReport getAverageRealisationTimeReport() {
        List<Order> orderList = databaseAccess.getAverageRealisationTimeReport();
        return countAverageRealisationTimeReport(orderList);
    }

    @Override
    public AverageDeliveryTimeReport getAverageDeliveryTimeReport() {
        List<Order> orderList = databaseAccess.getAverageDeliveryTimeReport();
        return countAverageDeliveryTimeReport(orderList);
    }

    @Override
    public byte[] createCompletedOrderPdf() {
        DefaultPieDataset dataSet = new DefaultPieDataset();

        CompletedOrderReport completedOrderReport = getCompletedOrderReport();
        for (CompletedOrderNode completedOrderNode : completedOrderReport.getNodes()) {
            dataSet.setValue(completedOrderNode.getRestaurant(), completedOrderNode.getCompletedOrders());
        }
        JFreeChart chart = ChartFactory.createPieChart(
                "Average Delivery Time", dataSet, true, true, false);
        return writeChartToPDF(chart, 500, 400, "D://barchart.pdf");
    }

    @Override
    public byte[] createDroppedOrderPdf() {
        DefaultPieDataset dataSet = new DefaultPieDataset();

        DroppedOrderReport droppedOrderReport = getDroppedOrderReport();


        for(DroppedOrderNode droppedOrderNode : droppedOrderReport.getNodes()) {
            dataSet.setValue(droppedOrderNode.getRestaurant(), droppedOrderNode.getDroppedOrders());
        }
        JFreeChart chart = ChartFactory.createPieChart(
                "Average Delivery Time", dataSet, true, true, false);
        return writeChartToPDF(chart, 500, 400, "D://barchart.pdf");
    }

    @Override
    public byte[] createAverageDeliveryTimePdf() {
        DefaultCategoryDataset dataSet = new DefaultCategoryDataset ();

        AverageDeliveryTimeReport averageDeliveryTimeReport = getAverageDeliveryTimeReport();


        for(AverageDeliveryTimeNode averageDeliveryTimeNode : averageDeliveryTimeReport.getNodes()) {
            dataSet.setValue( averageDeliveryTimeNode.getAverageDeliveryTime(), Long.toString(averageDeliveryTimeNode.getAverageDeliveryTime()),averageDeliveryTimeNode.getCity());
        }

        JFreeChart chart = ChartFactory.createBarChart(
                "Czas dostawy", "Miasto", "Czas",
                dataSet, PlotOrientation.VERTICAL, false, true, false);
        return writeChartToPDF(chart, 500, 400, "D://barchart.pdf");
    }

    @Override
    public byte[] createAverageRealisationTimePdf() {
        DefaultCategoryDataset dataSet = new DefaultCategoryDataset();
        AverageRealisationTimeReport averageRealisationTimeReport = getAverageRealisationTimeReport();


        for(AverageRealisationTimeNode averageRealisationTimeNode : averageRealisationTimeReport.getNodes()) {
            dataSet.setValue(averageRealisationTimeNode.getAverageRealisationTime(), Long.toString(averageRealisationTimeNode.getAverageRealisationTime()),averageRealisationTimeNode.getCity());
        }
        JFreeChart chart = ChartFactory.createBarChart(
                "Czas dostawy", "Miasto", "Czas",
                dataSet, PlotOrientation.VERTICAL, false, true, false);
        return writeChartToPDF(chart, 500, 400, "D://barchart.pdf");
    }


/*    @Override
    public void temp(int reportId) {
        DefaultPieDataset dataSet = new DefaultPieDataset();

        if(reportId == 1 ){
            CompletedOrderReport completedOrderReport = getCompletedOrderReport();
            for(CompletedOrderNode completedOrderNode : completedOrderReport.getNodes()) {
                dataSet.setValue(completedOrderNode.getRestaurant(), completedOrderNode.getCompletedOrders());
            }
        }else if(reportId == 2){
            DroppedOrderReport droppedOrderReport = getDroppedOrderReport();


            for(DroppedOrderNode droppedOrderNode : droppedOrderReport.getNodes()) {
                dataSet.setValue(droppedOrderNode.getRestaurant(), droppedOrderNode.getDroppedOrders());
            }

        }else if(reportId == 3){
            AverageRealisationTimeReport averageRealisationTimeReport = getAverageRealisationTimeReport();


            for(AverageRealisationTimeNode averageRealisationTimeNode : averageRealisationTimeReport.getNodes()) {
                dataSet.setValue(averageRealisationTimeNode.getCity(), averageRealisationTimeNode.getAverageRealisationTime());
            }

        }else if(reportId == 4){
            AverageDeliveryTimeReport averageDeliveryTimeReport = getAverageDeliveryTimeReport();


            for(AverageDeliveryTimeNode averageDeliveryTimeNode : averageDeliveryTimeReport.getNodes()) {
                dataSet.setValue(averageDeliveryTimeNode.getCity(), averageDeliveryTimeNode.getAverageDeliveryTime());
            }

        }else if(reportId == 5){
            CompletedOrderReport completedOrderReport = getCompletedOrderReport();

            for(CompletedOrderNode completedOrderNode : completedOrderReport.getNodes()) {
                dataSet.setValue(averageDeliveryTimeNode.getCity(), averageDeliveryTimeNode.getAverageDeliveryTime());
            }

        }else if(reportId == 6){
            AverageDeliveryTimeReport averageDeliveryTimeReport = getAverageDeliveryTimeReport();

            for(AverageDeliveryTimeNode averageDeliveryTimeNode : averageDeliveryTimeReport.getNodes()) {
                dataSet.setValue(averageDeliveryTimeNode.getCity(), averageDeliveryTimeNode.getAverageDeliveryTime());
            }
        }

        JFreeChart chart = ChartFactory.createPieChart(
                "Average Delivery Time", dataSet, true, true, false);
        writeChartToPDF(chart, 500, 400, "D://barchart.pdf");
    }*/

    public static byte[] writeChartToPDF(JFreeChart chart, int width, int height, String fileName) {
        PdfWriter writer = null;

        Document document = new Document();
        ByteArrayOutputStream stream = new ByteArrayOutputStream();

        try {

            writer = PdfWriter.getInstance(document, stream);
            document.open();
            PdfContentByte contentByte = writer.getDirectContent();
            PdfTemplate template = contentByte.createTemplate(width, height);
            Graphics2D graphics2d = template.createGraphics(width, height, new DefaultFontMapper());
            Rectangle2D rectangle2d = new Rectangle2D.Double(0, 0, width, height);

            chart.draw(graphics2d, rectangle2d);

            graphics2d.dispose();
            contentByte.addTemplate(template, 0, 0);


        } catch (Exception e) {
            e.printStackTrace();
        }
        document.close();
        return stream.toByteArray();
    }

    private CompletedOrderReport prepareCompletedOrderReport() {

        List<Order> orderList = databaseAccess.getCompletedOrderReport();
        return countCompletedOrders(orderList);

    }

    private DroppedOrderReport prepareDroppedOrderReport() {

        List<Order> orderList = databaseAccess.getDroppedOrderReport();
        return countDroppedOrders(orderList);
    }

    public AverageRealisationTimeReport countAverageRealisationTimeReport(List<Order> orderList){
        AverageRealisationTimeReport averageRealisationTimeReport = new AverageRealisationTimeReport();
        List<AverageRealisationTimeNode> nodes = new LinkedList<>();
        List<CounterObjectForReport> counterObjectForReports = new LinkedList<>();

        boolean isNode;
        for (Order order : orderList) {

            isNode = false;
            if (counterObjectForReports.isEmpty()) {
                counterObjectForReports.add(new CounterObjectForReport(order.getRealisationTime(),order.getCity(), 1));
                continue;
            }
            for (CounterObjectForReport counterObjectForReport: counterObjectForReports) {
                if (order.getCity().equals(counterObjectForReport.getCity())) {
                    counterObjectForReport.setTime(counterObjectForReport.getTime() + order.getRealisationTime());
                    counterObjectForReport.setCounter(counterObjectForReport.getCounter() + 1);
                    isNode = true;
                }
            }
            if (isNode == false) {
                counterObjectForReports.add(new CounterObjectForReport(order.getRealisationTime(),order.getCity(), 1));
            }
        }
        for(CounterObjectForReport counterObjectForReport: counterObjectForReports){
            nodes.add(new AverageRealisationTimeNode(counterObjectForReport.getTime()/counterObjectForReport.getCounter(),counterObjectForReport.getCity()));
        }
        averageRealisationTimeReport.setNodes(nodes);
        return averageRealisationTimeReport;

    }

    public AverageDeliveryTimeReport countAverageDeliveryTimeReport(List<Order> orderList){
        AverageDeliveryTimeReport averageDeliveryTimeReport = new AverageDeliveryTimeReport();
        List< AverageDeliveryTimeNode> nodes = new LinkedList<>();
        List<CounterObjectForReport> counterObjectForReports = new LinkedList<>();

        boolean isNode;
        for (Order order : orderList) {

            isNode = false;
            if (counterObjectForReports.isEmpty()) {
                counterObjectForReports.add(new CounterObjectForReport(order.getDeliveryTime(),order.getCity(), 1));
                continue;
            }
            for (CounterObjectForReport counterObjectForReport: counterObjectForReports) {
                if (order.getCity().equals(counterObjectForReport.getCity())) {
                    counterObjectForReport.setTime(counterObjectForReport.getTime() + order.getDeliveryTime());
                    counterObjectForReport.setCounter(counterObjectForReport.getCounter() + 1);
                    isNode = true;
                }
            }
            if (isNode == false) {
                counterObjectForReports.add(new CounterObjectForReport(order.getDeliveryTime(),order.getCity(), 1));
            }
        }
        for(CounterObjectForReport counterObjectForReport: counterObjectForReports){
            nodes.add(new  AverageDeliveryTimeNode(counterObjectForReport.getTime()/counterObjectForReport.getCounter(),counterObjectForReport.getCity()));
        }
        averageDeliveryTimeReport.setNodes(nodes);
        return averageDeliveryTimeReport;

    }

    public CompletedOrderReport countCompletedOrders(List<Order> orderList){
        CompletedOrderReport completedOrderReport = new CompletedOrderReport();
        List<CompletedOrderNode> nodes = new LinkedList<>();
        boolean isNode;
        for (Order order : orderList) {

            isNode = false;
            if (nodes.isEmpty()) {
                nodes.add(new CompletedOrderNode(order.getCity(), 1));
                continue;
            }
            for (CompletedOrderNode completedOrderNode : nodes) {
                if (order.getCity().equals(completedOrderNode.getRestaurant())) {
                    completedOrderNode.setCompletedOrders(completedOrderNode.getCompletedOrders() + 1);
                    isNode = true;
                }
            }
            if (isNode == false) {
                nodes.add(new CompletedOrderNode(order.getCity(), 1));
            }
        }
        completedOrderReport.setNodes(nodes);
        return completedOrderReport;

    }
    public DroppedOrderReport countDroppedOrders(List<Order> orderList){
        DroppedOrderReport droppedOrderReport= new DroppedOrderReport();
        List<DroppedOrderNode> nodes = new LinkedList<>();
        boolean isNode;
        for (Order order : orderList) {

            isNode = false;
            if (nodes.isEmpty()) {
                nodes.add(new DroppedOrderNode(order.getCity(), 1));
                continue;
            }
            for (DroppedOrderNode droppedOrderNode : nodes) {
                if (order.getCity().equals(droppedOrderNode.getRestaurant())) {
                    droppedOrderNode.setDroppedOrders(droppedOrderNode.getDroppedOrders() + 1);
                    isNode = true;
                }
            }
            if (isNode == false) {
                nodes.add(new DroppedOrderNode(order.getCity(), 1));
            }
        }
        droppedOrderReport.setNodes(nodes);
        return droppedOrderReport;
    }


}
