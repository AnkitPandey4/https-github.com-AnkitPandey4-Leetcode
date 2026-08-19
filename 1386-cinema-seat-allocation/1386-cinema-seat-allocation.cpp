class Solution {
public:
    int maxNumberOfFamilies(int n, vector<vector<int>>& reservedSeats) {
        
        unordered_map<int, int> rowReservations;
      
        
        for (auto& reservation : reservedSeats) {
            int row = reservation[0];
            int seatNumber = reservation[1];
            rowReservations[row] |= 1 << (10 - seatNumber);
        }
      
        
        int seatGroupMasks[3] = {0b0111100000, 0b0000011110, 0b0001111000};
      
        
        int totalFamilies = (n - rowReservations.size()) * 2;
      
        for (auto& [rowNumber, reservedBitmask] : rowReservations) {
            for (int& mask : seatGroupMasks) {
                if ((reservedBitmask & mask) == 0) {
                    reservedBitmask |= mask;
                    totalFamilies++;
                }
            }
        }
      
        return totalFamilies;
    }
};
