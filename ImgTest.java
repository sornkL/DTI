import java.io.*;
import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.stream.Collectors;
import java.util.stream.Stream;

//@SpringBootTest(classes = App.class)
//@RunWith(SpringRunner.class)
public class ImgTest {
      public static String[] split(String s, char c) {
            int ln = s.length();
            int i = 0;

            int cnt;
            for(cnt = 1; (i = s.indexOf(c, i)) != -1; ++i) {
                ++cnt;
            }

            String[] res = new String[cnt];
            i = 0;

            int e;
            for(int b = 0; b <= ln; b = e + 1) {
                e = s.indexOf(c, b);
                if (e == -1) {
                    e = ln;
                }

                res[i++] = s.substring(b, e);
            }

            return res;
      }

      public static void test(){
            String[] columnName = {
                    "BindingDB Reactant_set_id",
                    "Ligand SMILES",
                    "IC50 (nM)",
                    "Kd (nM)",
                    "BindingDB Target Chain  Sequence",
                    "PDB ID(s) of Target Chain",
                    "UniProt (SwissProt) Primary ID of Target Chain",
                    "UniProt (SwissProt) Secondary ID(s) of Target Chain",
                    "UniProt (TrEMBL) Primary ID of Target Chain",
                    "UniProt (TrEMBL) Secondary ID(s) of Target Chain\n"};
            int[] columnFilter = new int[]{0,1,9,10,37,38,41,42,46,47};
            String in = "BindingDB_All.tsv";
            String out = "out.csv";
            int limit = Integer.MAX_VALUE;

            File file = new File(in);
            File outFile = new File(out);
            try(BufferedReader reader = new BufferedReader(new InputStreamReader(new FileInputStream(file)));
                BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(new FileOutputStream(outFile)));) {

                String ignoreHeader = reader.readLine();
                writer.write(String.join(",", columnName));

                String[] columns = new String[columnFilter.length];
                int count = 0;
                String line;
                while(count < limit && (line = reader.readLine()) != null){
                    String[] tokens = split(line,'\t');
                    for (int i = 0; i < columnFilter.length; i++) {
                        String trimmed = tokens[columnFilter[i]].trim();
                        columns[i] = "\"" + (trimmed.length() == 0 ? "null" : trimmed) + "\"";
                    }
                    writer.write(String.join(",", columns));
                    writer.write("\n");
                    count++;
                }
            } catch (IOException e) {
                e.printStackTrace();
            }
      }

   public static void main(String[] args) {
        test();
   }

}
