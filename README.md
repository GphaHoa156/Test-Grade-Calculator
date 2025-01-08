# Test-Grade-Calculator

Auto Grading System<
    <h1>Auto Grading System</h1>
    <p>
        This project provides an automated system to grade student exams based on a provided answer key and a file containing student responses.
    </p>

    <h2>Features</h2>
    <ul>
        <li>Analyze student response files and identify invalid entries.</li>
        <li>Calculate grades for valid entries based on the provided answer key.</li>
        <li>Generate descriptive statistics about grades and question performance.</li>
        <li>Export the results to a file and compare with expected output for validation.</li>
    </ul>

    <h2>How to Run the Script</h2>

    <h3>Prerequisites</h3>
    <p>Ensure you have the following installed:</p>
    <ul>
        <li>Python 3.6 or higher</li>
        <li>Required libraries: <code>pandas</code>, <code>numpy</code></li>
    </ul>
    <pre><code>pip install pandas numpy</code></pre>

    <h3>Steps to Run</h3>
    <ol>
        <li>
            <strong>Clone the Repository:</strong>
            <p>Download or clone the repository to your local machine.</p>
        </li>
        <li>
            <strong>Prepare Input Files:</strong>
            <p>
                Ensure your input files (e.g., <code>class1.txt</code>, <code>class2.txt</code>, etc.) are in the same directory as the script.
                These files should contain student responses in the format:
            </p>
            <pre><code>Nxxxxxxxx,A,B,C,D,...</code></pre>
        </li>
        <li>
            <strong>Run the Script:</strong>
            <p>Execute the script in the terminal:</p>
            <pre><code>python lastname_firstname_grade_the_exams.py</code></pre>
        </li>
        <li>
            <strong>Enter the File to Grade:</strong>
            <p>When prompted, enter the name of the class file without the <code>.txt</code> extension. For example:</p>
            <pre><code>Enter a class to grade (i.e. class1 for class1.txt): class1</code></pre>
        </li>
        <li>
            <strong>View Results:</strong>
            <p>The script will analyze the file, grade the responses, and print statistics. The graded results will be saved in a file named <code>&lt;class_name&gt;_grades.txt</code>.</p>
        </li>
        <li>
            <strong>Compare Results:</strong>
            <p>The script will compare the output file with the expected output in the <code>Expected Output</code> folder.</p>
        </li>
    </ol>

    <h2>Output Example</h2>
    <h3>Console Output</h3>
    <pre class="output">
**** ANALYZING ****

does not contain exactly 26 values:
N12345678,A,B,C

N# is invalid: 
N1234567,A,B,C,D,...

**** REPORT ****
Total valid lines of data: 10
Total invalid lines of data: 2

Total student of high scores: 5
Mean (average) score: 85.0
Highest score: 95
Lowest score: 70
Range of scores: 25
Median score: 85
Question that most people skip: 5 - 3 - 0.300
Question that most people answer incorrectly: 8 - 4 - 0.400
    </pre>

    <h3>Generated File</h3>
    <p><code>class1_grades.txt</code>:</p>
    <pre><code>
N12345678,90
N23456789,85
...
    </code></pre>

    <h2>Contact</h2>
    <p>If you encounter any issues, feel free to reach out for assistance.</p>
</body>
</html>
