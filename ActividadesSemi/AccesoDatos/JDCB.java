import java.sql.*;

public class ListarProductos {
    static final String URL = "jdbc:mysql://localhost:3306/tienda";
    static final String USER = "tienda_app";
    static final String PASS = "ClaveTienda_2026!";

    public static void main(String[] args) {
        try {
            Class.forName("com.mysql.cj.jdbc.Driver"); // buena práctica
        } catch (ClassNotFoundException e) {
            System.err.println("No se encuentra el conector MySQL. ¿Está en el pom.xml?");
            return;
        }

        String sql = "SELECT id, nombre, precio, stock FROM producto";
        try (Connection con = DriverManager.getConnection(URL, USER, PASS);
             Statement st = con.createStatement();
             ResultSet rs = st.executeQuery(sql)) {

            System.out.printf("%-4s %-20s %8s %6s%n", "ID", "NOMBRE", "PRECIO", "STOCK");
            while (rs.next()) {
                System.out.printf("%-4d %-20s %8.2f %6d%n",
                        rs.getLong("id"), rs.getString("nombre"),
                        rs.getDouble("precio"), rs.getInt("stock"));
            }
        } catch (SQLException e) {
            System.err.println("Error SQL (" + e.getSQLState() + "): " + e.getMessage());
        }
    }
}
