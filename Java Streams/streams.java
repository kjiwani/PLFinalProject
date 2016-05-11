// to run: /Users/Luna/Programming-Languages/CarnotKEdist/dist/bin/jython mini-lisp.py

// ml> (exec 'import streams; toReturn = streams.DoStream([5, 10, 15])')



import java.util.List;
import java.util.ArrayList;
public class streams {
  public static class Person{
    private int age_;

    public Person(int age){
      age_ = age;
    }

    public int GetAge(){
      return age_;
    }
  }

  public static int DoStream(int[] ages){
    List<Person> people = new ArrayList<Person>();
    for(int e : ages)
      people.add(new Person(e));
    return StreamOps(people);
  }

  public static int StreamOps(List<Person> my_people){
    int ageSum = my_people.stream()
      .reduce(0, (sum, p) -> sum += p.GetAge(), (sum1, sum2) -> sum1 + sum2);

    return ageSum;
  }
}

