import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.Collector;

public class ListComprehension {
    static class Person {
        int age;
        
        Person(int age) {
            this.age = age;
        }
    }
    
    public static void main(String[] args) {
        List<Person> persons =
            Arrays.asList(
                new Person(18),
                new Person(12));
        
    }
    
    private static void streamops(List<Person> persons) {
        Integer ageSum = persons
            .stream()
            .reduce(0, (sum, p) -> sum += p.age, (sum1, sum2) -> sum1 + sum2);
        
        System.out.println(ageSum);
        
    }
}
