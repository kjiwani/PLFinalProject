import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.Collector;
import java.util.Arrays;
import java.util.List;

public class ListComprehension {
    
    static class Person {
        int age;
        
        Person(int age) {
            this.age = age;
        }
    }
    
    public int addPerson(String[] args) {

        List<Person> persons = 
            Arrays.asList(
                new Person(18),
                new Person(12));
        
        
        int ages = streamops(persons);
        
        return ages;
        
    }
    
    public int streamops (List<Person> persons) {
    
        Integer ageSum = persons
            .stream()
            .reduce(0, (sum, p) -> sum += p.age, (sum1, sum2) -> sum1 + sum2);
        
        return ageSum;
        
    }
}
