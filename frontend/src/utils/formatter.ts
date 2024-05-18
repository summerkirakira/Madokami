export function formatBytes(bytes: number, decimals: number = 2): string {
    if (bytes === 0) return '0 Bytes';
  
    const k: number = 1024;
    const dm: number = decimals < 0 ? 0 : decimals;
    const sizes: string[] = ['Bytes', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'];
  
    const i: number = Math.floor(Math.log(bytes) / Math.log(k));
  
    return parseFloat((bytes / Math.pow(k, i)).toFixed(dm)) + ' ' + sizes[i];
  }
  

  export function convertCronToMinutes(cron: string | null): number | null {
    if (!cron) {
      return 0;
    }
    try {
      const cronParts = cron.split(' ');
      const minutes = parseInt(cronParts[0].split('/')[1]);
      return minutes;
    } catch (e) {
      return null;
    }
    
  }

  export function convertMinutesToCron(minutes: number): string | null {
    if (minutes <= 0) {
      return null;
    }
    return `*/${minutes} * * * *`;
  }