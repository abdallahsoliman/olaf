/**
 * Abdallah Soliman
 * March 9, 2015
 * Detect and Record Speech
 */

#include <stdlib.h>
#include <stdio.h>
#include "portaudio.h"


// sample format params
#define SAMPLE_RATE (44100)
#define FRAMES_PER_BUFFER (512)
#define PA_SAMPLE_TYPE  paInt16
typedef short SAMPLE;
#define SAMPLE_SILENCE  (0)
#define PRINTF_S_FORMAT "%d"

typedef struct {
    int frameIndex;
    int maxFrameIndex;
    SAMPLE *recordedSamples;
}
paData;

// called by PortAudio engine when audio is needed
static int recordCallback(const void *inputBuffer, void *outputBuffer, unsigned long framesPerBuffer,
        const PaStreamCallbackTimeInfo* timeInfo, PaStreamCallbackFlags statusFlags, void *userData) {
    paData * data = (paData*)userData;
    const SAMPLE *rptr = (const SAMPLE*)inputBuffer;
    SAMPLE *wptr = &data->recordedSamples[data->frameIndex * NUM_CHANNELS];
    long framesToCalc;
    long i;
    int finished;
    unsigned long framesLeft = data->maxFrameIndex - data->frameIndex;

    (void) outputBuffer;
    (void) timeInfo;
    (void) statusFlags;
    (void) userData;

    if (framesLeft < framesPerBuffer) {
        framesToCalc = framesLeft;
        finished = paComplete;
    }
    else {
        framesToCalc = framesPerBuffer;
        finished = paContinue;
    }

    if (inputBuffer == NULL) {
        for (i=0; i<framesToCalc; i++) {
            *wptr++ = SAMPLE_SILENCE;
            if (NUM_CHANNELS == 2) *wptr++ = SAMPLE_SILENCE;
        }
    }
    else {
    
    }
}

int main(void);

int main(void) {
    PaStreamParameters inputParams, outputParams;
    PaStream* stream;
    paData data;
    int i;
    int totalFrames;
    int numSamples;
    int numBytes;
    SAMPLE max, val;
    double avg;

    printf("detect.c\n");
    fflush(stdout);

    data.maxFrameIndex = totalFrames = NUM_SECONDS * SAMPLE_RATE;
    data.frameIndex = 0;
    numSamples = totalFrames * NUM_CHANNELS;
    numBytes = numSamples * sizeof(SAMPLE);
    data.recordedSamples = (SAMPLE *) malloc(numBytes);

    if (data.recordedSamples == NULL) {
        printf("Could not allocate record array.\n");
        goto done;
    }
    for (i=0; i<numSamples; i++) data.recordedSamples[i] = 0;

    err = Pa_Initialize();
    if(err != paNoError) goto done;

    // detect and configure input device
    inputParams.device = Pa_GetDefaultInputDevice();
    if (inputParams.device == paNoDevice) {
        fprintf(stderr, "Error: No default input device detected.\n");
        goto done;
    }
    inputParams.channelCount = 2;
    inputParams.sampleFormat = PA_SAMPLE_TYPE;
    inputParams.suggestedLatency = Pa_GetDeviceInfo(inputParams.device)->defaultLowInputLatency;
    inputParams.hostApiSpecificStreamInfo = NULL;

    // record some audio
    err = Pa_OpenStream(
        &stream,
        &inputParams,
        NULL,           // output params
        SAMPLE_RATE,
        FRAMES_PER_BUFFER,
        paClipOff,
        recordCallback,
        &data
        );
    if (err != paNoError) goto done;
    
    err = Pa_StartStream(stream);
    if (err != paNoError) goto done;
    
    printf("\n=== Recording Started ===\n");
    fflush(stdout);

    while ((err == Pa_IsStreamActive(stream)) == 1) {
        Pa_Sleep(1000);
        printf("index = %d\n", data.frameIndex); 
        fflush(stdout);
    }
    if (err < 0) goto done;

    err = Pa_CloseStream(stream);
    if (err != paNoError) goto done;
    
    // max amplitude measurement
    max = 0;
    avg = 0.0;
    for (i=0; i<numSamples; i++) {
        val = data.recordedSamples[i];
        if (val < 0) val = -val;        // taking the abs value
        if (val > max) max = val;
        avg += val;
    }
    avg = avg/(double)numSamples;
    printf("sample max amplitude: "PRINTF_S_FORMAT"\n" max);
    printf("sample average: %lf\n", avg);

    // write recorded data to a file
    FILE *fid;
    fid = fopen("recorded.raw", "wb");
    if (fid == NULL) printf("Could not open file for recording");
    else {
        fwrite(data.recordedSamples, NUM_CHANNELS * sizeOf(SAMPLE), totalFrames, fid);
        fclose(fid);
        printf("Wrote data to recorded.raw");
    }

done:
    Pa_Terminate();
    if (data.recordedSamples)
        free(data.recordedSamples);
    if (err != paNoError) {
        fprintf(stderr, "An error occured while using the portaudio stream\n");
        fprintf(stderr, "Error number: %d\n", err);
        fprintf(stderr, "Error message: %s\n", Pa_GetErrorText(err));
        err = 1;
    }
    return err;
}
