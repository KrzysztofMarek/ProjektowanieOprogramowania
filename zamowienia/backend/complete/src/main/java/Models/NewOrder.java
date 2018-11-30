package Models;

import java.sql.Date;
import java.util.ArrayList;

public class NewOrder {

    public Integer id_klienta;
    public Integer id_restauracji;
    public ArrayList<OrderItem> lista_dan;
    public double kwota;
    public String adres;
}