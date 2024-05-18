import { SchedulerApi } from "@/client";
import { getToken } from "@/utils/tokenManager";


const scheduleApi = new SchedulerApi();

export async function getSchedules() {
    const token = getToken();
    if (!token) {
        throw new Error("User not logged in");
    }
    return await scheduleApi.getAllSchedulesV1ScheduleAllGet(token);
}

export async function updateSchedule(scheduleId: number, cron_str: string | null) {
    const token = getToken();
    if (!token) {
        throw new Error("User not logged in");
    }
    return await scheduleApi.updateScheduleV1ScheduleUpdatePost(token, {schedule_id: scheduleId, cron_str});
}

export async function restartScheduler() {
    const token = getToken();
    if (!token) {
        throw new Error("User not logged in");
    }
    return await scheduleApi.restartSchedulerV1ScheduleRestartGet(token);
}