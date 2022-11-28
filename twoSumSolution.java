class twoSumSolution{
    public int[] twoSum(int[] nums, int target){

        int indiceArray[] = new int[2];
        boolean found = false;
        
        for(int i=0;i<(nums.length-1);++i){
                
            for(int y=i+1;y<=nums.length-1;++y){
                if(nums[i]+nums[y]==target){
                    indiceArray[0] = i;
                    indiceArray[1] = y;
                    found = true;
                }
            }
            
            if(found==true){
                break;
            }

        }

        return indiceArray;
    }
    
}
