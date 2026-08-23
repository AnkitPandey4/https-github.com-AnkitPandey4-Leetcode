class Solution {
    public boolean sumGame(String num) {
        int n = num.length();
        int leftSum = 0, rightSum = 0;
        int leftQuestionMarks = 0, rightQuestionMarks = 0;

        for (int i = 0; i < n / 2; i++) {
            char c = num.charAt(i);
            if (c == '?') {
                leftQuestionMarks++;
            } else {
                leftSum += c - '0';
            }
        }

        for (int i = n / 2; i < n; i++) {
            char c = num.charAt(i);
            if (c == '?') {
                rightQuestionMarks++;
            } else {
                rightSum += c - '0';
            }
        }

        
        int sumDiff = leftSum - rightSum;
        int qmDiff = leftQuestionMarks - rightQuestionMarks;

        
        return sumDiff + (qmDiff * 9) / 2 != 0 || (qmDiff % 2 != 0);
    }
}
